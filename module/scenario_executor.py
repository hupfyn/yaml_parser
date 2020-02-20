from module import browser_action_handler
import copy


def exec_action(type, value):
    check_type[str(type).lower()](value)


def steps_execute(steps):
    for step in steps:
        step_type = list(step.keys()).pop()
        step_value = list(step.values()).pop()
        exec_action(step_type, step_value)


def run_test(test_name, test_actions):
    print(f'start test: {test_name}')
    for action_type, action_value in test_actions.items():
        exec_action(action_type, action_value)
    browser_action_handler.check_is_page_load()
    print(f'stop test: {test_name}')


def run_parametrized_test(test_name, test_actions):
    parameters = test_actions.pop('parameters')
    for parameter in parameters:
        parametrised_test_actions = copy.deepcopy(test_actions)
        parametrised_test_actions["url"] = parametrised_test_actions.get('url') + parameter
        run_test(str(f'{test_name}_{(parameters.index(parameter)+1)}'), parametrised_test_actions)


def run_scenario(scenario):
    for test_name, test_actions in scenario.items():
        if 'parameters' in test_actions.keys():
            run_parametrized_test(test_name, test_actions)
        else:
            run_test(test_name, test_actions)


check_type = {
    "url": browser_action_handler.open_url,
    "steps": steps_execute,
    "check": browser_action_handler.check_element,
    "input": browser_action_handler.input_data,
    "click": browser_action_handler.click_element,
    "execute_js": browser_action_handler.execute_js
}
