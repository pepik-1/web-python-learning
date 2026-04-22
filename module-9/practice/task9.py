# service|max_retries|timeout_sec|environment|enabled
rows = [
    'auth|3|1.5|prod|on',
    'billing|0|2.0|stage|on',
    'search|two|0.8|dev|off',
    'media|5|-1|prod|on',
    'chat|4|1.2|test|off',
    'mail|2|0.5|stage|maybe',
    'worker|1|3.4|prod|on',
]


class DeployConfigError(Exception):
    pass


class RowFormatError(DeployConfigError):
    pass


class RetriesError(DeployConfigError):
    pass


class TimeoutError(DeployConfigError):
    pass


class EnvironmentError(DeployConfigError):
    pass


class EnabledFlagError(DeployConfigError):
    pass


def parse_config(row):
    service ,max_retries, timeout_sec, environment, enabled = row.split('|')
    acceptable_env = {'prod','stage','dev'}
    try:
        len(row.split('|')) == 5
    except ValueError as e:
        raise RowFormatError('wrong format') from e
    


    if enabled not in {'on','off'}:
        raise EnabledFlagError('it`s off')
    if enabled == 'on':
        enabled = True
    if enabled == 'off':
        enabled = False

    try:
        max_retries = int(max_retries)
        if max_retries < 0:
            raise RetriesError('wrong retries format')
    except ValueError as e:
        raise RetriesError('wrong retries format') from e
    
    try:
        timeout_sec = float(timeout_sec)
        if timeout_sec < 0:
            raise TimeoutError('wrong timeout format')
    except ValueError as e:
        raise TimeoutError('wrong timeout format') from e
    
    try:
        
        if environment not in acceptable_env:
            raise EnvironmentError('wrong Enviroment')
    except ValueError as e:
        raise EnvironmentError('wrong Enviroment') from e
    
        
    
    

    return {'service':service ,'max_retries':max_retries, 'timeout_sec':timeout_sec, 'environment':environment, 'enabled':enabled}
    # TODO: распарсить строку и провалидировать max_retries, timeout_sec, environment, enabled
    # TODO: при ошибках конвертации использовать raise ... from ...
    # TODO: enabled вернуть как bool
    

def load_configs(rows):
    configs = []
    errors = []
    for el in rows:
        try:
            
            result = parse_config(el)
            configs.append(result)
        except DeployConfigError as e:
            errors.append((el,type(e).__name__,e))
            
    return configs,errors

    # TODO: вернуть (configs, errors)
    
load = load_configs(rows)
config,errors = load
print(len(config),len(errors))
print(errors)
print(config)
# TODO: вызвать load_configs(rows)
# TODO: вывести число валидных конфигов и число ошибок
# TODO: вывести ошибки по типам
types = {}
for _,err,_ in errors:
    types[err] = types.get(err,0) +1
print(types)

# TODO: собрать enabled_by_environment: dict[str, list[str]]

enabled_by_enviroment = {}
for conf in config:

    enabled_by_enviroment[conf['environment']] = [*enabled_by_enviroment.get(conf['environment'],[]),config]

print(enabled_by_enviroment)

# TODO: посчитать average_timeout только по enabled=True

average_timeout = sum(conf['timeout_sec'] for conf in config if conf['environment']) / len(config)
print(average_timeout)
    