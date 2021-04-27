#   https://docs.python.org/3/library/asyncio.html


# Python provides 3 main ways for a python programmer to achieve concurrent codes.
# Namely:
#   >   'multiprocessing' module
#   >   'multithreading' module
#   >   'asyncio' module
#
# In this note, asyncio will be discussed

#########################################
#   Asyncio - When is it suitable?
#########################################
#
#   Although asyncio helps us achieve concurrency, it actually still
#   runs single threaded, and no multicores are utilized. It is just
#   able to switch context between different tasks scheduled to it by
#   programmer, achieving the concurrency effect
#
#   As the name implies, it is best used in case of IO-bound scenarios
#   especially in high-level structured network code
#
#   Quick Glossary:
#       There are 2 types of bounds: IO-bound and CPU-bound
#
#       CPU bound are simply slow codes that heavily depends on the CPU
#       clock speed. If the CPU is sped up, surely the program will also
#       speed up. Eg: calculating prime numbers or working on long list of
#       numbers
#
#       IO-bound are simply slow codes that depends on IO. For example, waiting
#       for server to make a respond, or user to enter something. Speeding up the
#       CPU won't help speeding up the code in this case.


#####################################
#    Event Loop - The core of Asyncio
#####################################
#   Abstractly, how asyncio works can be thought as a giant loop with scheduled
#   tasks.
#   The task that is currently focused on, is called current context.
#
#   While executing the coroutines currently focused, if the event loop encounters
#   an 'await' keyword, it intelligently knows that the code is going to take some
#   time to complete.
#   Therefore, what it does is to switch the context to execute the other scheduled
#   tasks, until the previous 'await' code is completed, then only it switches the
#   context back to the code.
#
#   Since event loop is thought as a loop, if you run it in synchronous code, the loop
#   is going to block there, unless you exited the loop, of course



###################################
#   Awaitables
###################################
#   To use Asyncio module, there are these important keywords:
#       >   async
#       >   await
#   Kind of like Javascript right? Yes
#
#   Objects that can be awaited are called awaitables. There are 3 types of awaitables:
#
#       >   Coroutines
#           Simply is a function marked using async. When awaited, the context immediately
#           switches into the coroutine, and only switches back after coroutine is done
#
#       >   Tasks
#           Tasks are codes that are meant to run concurrently. Done via asyncio.create_task( async func )
#           The Task will be scheduled
#           If the task is awaited, then it will block execution until the task is complete
#
#       >   Futures
#           Like tasks but with return values. Identical to Promises in Javascript.
#
#   The program shall be run in an event loop, done via asyncio.run( coroutine )
#   Tasks are created via asyncio.create_task( coroutine ) and returns a Task object. Need to be
#   awaited later
#   Futures are usually returned by other modules. We use future executing functions like asyncio.gather( futures...)



import asyncio

#############################################
# Coroutine example - Context switching
#############################################
async def wait1Sec():
    await asyncio.sleep(1)
    print("Waited for 1 second!")
    await wait2Sec()
    print("Exiting wait1Sec")


async def wait2Sec():
    await asyncio.sleep(2)
    print("Waited for 2 second!")
    await wait3Sec()
    print("Exiting wait2Sec")


async def wait3Sec():
    await asyncio.sleep(3)
    print("Waited for 3 Second!")
    print("Exiting wait3Sec")


# As above example, you would expect the program to run as follows:
#   Enters wait1Sec()
#   >   Wait 1 sec
#   >   Print "Waited for 1 second"
#   >   Enters wait2Sec()
#       >   Wait 2 sec
#       >   Print "Waited for 2 second"
#       >   Enters wait3Sec()
#           >   Wait 3 sec
#           >   Print "Waited for 3 second"
#           >   Print "Exiting wait3Sec"
#       >   Print "Exiting wait2Sec"
#   >   Print "Exiting wait1Sec"

asyncio.run( wait1Sec() )       # Comment this if you want skip concurrent example



################################
#   Task Example
################################
# Please notice we DO NOT AWAIT tasks here.
# If awaited, they will be blocking, just like coroutines
async def wait1Task():
    await asyncio.sleep(1)
    print("Sleeped for 1 seconds")

async def wait2Task():
    asyncio.create_task( wait1Task() )
    await asyncio.sleep(2)
    print("Sleeped for 2 seconds")


async def wait3Task():
    asyncio.create_task( wait2Task() )
    await asyncio.sleep(3)
    print("Sleeped for 3 seconds")


asyncio.run( wait3Task() )



###############################
#   Futures Example - Promises
#   Can be done just like tasks
###############################


async def fetchMedia():
    await asyncio.sleep(2)
    return {"Titles": ["Avatar", 'Conjuring', 'Kong'] }


async def fetchPeople():
    await asyncio.sleep(1)
    return {"Names": ["John", 'Doe', 'Lily'] }


async def processRequest(req):
    # Futures are done like in this case, awaiting for return values
    if req == 'media':
        res = await fetchMedia()
    else:
        res = await fetchPeople()
    print(res)


# If the code is synchronous, the media which take 2 seconds will run first, then 1 second for people
async def main():
    reqs = (
        asyncio.create_task(processRequest('media') ),
        asyncio.create_task(processRequest('people') )
    )
    await asyncio.wait(reqs)


asyncio.run( main() )