from package.routines.routines_config import init_routines
from package.common.logger import logErr, logInfo
from package.routines.routine import Routine, RoutineFailure

if __name__ == '__main__':
    # Read config
    try:
        routines: list[Routine] = init_routines()
        for routine in routines:
            logInfo(f'Running {routine.id} ...')
            if not routine.run():
                raise RoutineFailure(f'Routine {routine.id} failed to complete successfully')
        print('End with success')
    except RoutineFailure as err:
        logErr(err)
        print(err)
        print('Check output/log for information')
    except Exception as err:
        logErr(err)
        print(f'Unknown error {type(err)}\n{err}')
        print('Check output/log for information')

