import cx_Freeze

executables = [ cx_Freeze.Executable('main.py') ]

cx_Freeze.setup(
    name='My Pong',
    options={
        "build_exe": {
            "packages": ["pygame"],
            "include_files": ['Sounds/BallHit.wav', 'Sounds/BallScore.wav', 'Sounds/menu.wav', 'Sounds/playing.wav',
                              'Sounds/victory.wav', 'Text/ArcadeFont.ttf' ]
        }
    },

    description = 'My Pong game',
    executables = executables

)