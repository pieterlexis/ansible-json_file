import testinfra.utils.ansible_runner
import json

runner = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory')

runner.options.connection = 'docker'

testinfra_hosts = runner.get_hosts('all')

def test_change_existing(Command):
    stdout = Command("cat /tmp/0.json").stdout
    data = json.loads(stdout)

    assert data['a'] == 'e'
    assert data['c'] == 'f'

def test_nested_change_existing(Command):
    stdout = Command("cat /tmp/1.json").stdout
    data = json.loads(stdout)

    assert data['c'] == {'d': 'f'}

def test_nested_addition_in_existing(Command):
    stdout = Command("cat /tmp/2.json").stdout
    data = json.loads(stdout)

    assert data['c'] == {'d': 'e', 'e': 'f'}

def test_new_nested_addition(Command):
    stdout = Command("cat /tmp/3.json").stdout
    data = json.loads(stdout)

    assert data == {'a': 'b', 'c': {'d': 'e'}, 'e': {'f': 'g'}}

def test_remove_exising(Command):
    stdout = Command("cat /tmp/4.json").stdout
    data = json.loads(stdout)

    assert data == {'c': {'d': 'e'}}

    stdout = Command("cat /tmp/6.json").stdout  # second-level
    data = json.loads(stdout)

    assert data == {'a': 'b', 'c': {}}

def test_remove_nonexising(Command):
    stdout = Command("cat /tmp/5.json").stdout
    data = json.loads(stdout)

    assert data == {'a': 'b', 'c': {'d': 'e'}}

    stdout = Command("cat /tmp/7.json").stdout
    data = json.loads(stdout)

    assert data == {'a': 'b', 'c': {'d': 'e'}}

def test_types(Command):
    stdout = Command("cat /tmp/8.json").stdout
    data = json.loads(stdout)

    assert data == {
        'a': 'b',
        'c': {'d': 'e'},
        'integer': 25,
        'bool1': True,
        'bool2': False,
        'should_be_null': None
    }

def test_dotted(Command):
    stdout = Command("cat /tmp/9.json").stdout
    data = json.loads(stdout)

    assert data == {
        'a': 'b',
        'c': {'d': 'e'},
        'a.b': 'bar',
        'd': {
            'a.b': 'buzz'
        }
    }

def test_types_as_string(Command):
    stdout = Command("cat /tmp/10.json").stdout
    data = json.loads(stdout)

    assert data == {
        'a': 'b',
        'c': {'d': 'e'},
        'integer': '25',
        'bool1': 'True',
        'bool2': 'False',
        'should_be_null': 'None'
    }
