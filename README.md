Ansible Library: json_file
==========================

A library module that allows modifying json files

[![Build Status](https://travis-ci.org/pieterlexis/ansible-json_file.svg?branch=master)](https://travis-ci.org/pieterlexis/ansible-json_file)

Requirements
------------

None

Dependencies
------------

None

Usage Examples
--------------
```yaml
- hosts: all
  tasks:
    - name: Change value of 'foo' to 'bar'
      json_file:
        dest: /etc/file.conf
        key: 'foo'
        value: 'bar'
```

This library supports nesting in the JSON by using a dot ('.') as the seperator in the key.
Consider the following file:
```json
{ "foo": {
    "bar": "buzz"
  }
}
```

Changing the value of "bar" to "whatever" is done like this:
```yaml
- hosts: all
  tasks:
    - name: Change value of 'bar' to 'whatever'
      json_file:
        dest: /etc/file.conf
        key: 'foo.bar'
        value: 'whatever'
```

Dots in key-names must be escaped:
```json
{ "foo.bar": "buzz" }
```

Can be modified thusly:
```yaml
- hosts: all
  tasks:
    - name: Change value of 'foo.bar' to 'whatever'
      json_file:
        dest: /etc/file.conf
        key: 'foo\.bar'
        value: 'whatever'
```

Setting a value to `null` is a little harder than you would expect due to a [bug in Ansible](https://github.com/ansible/ansible/issues/13877).
Set `value` to `None` to accomplish this:
```yaml
- hosts: all
  tasks:
    - name: Set 'foo' to null
      json_file:
        dest: /etc/file.conf
        key: 'foo'
        value: None
```

Sometimes, a number must be saved as a string in the resulting JSON file.
Setting the `as_string` argument to 'yes' will ensure this:

```yaml
- hosts: all
  tasks:
    - name: Set 'foo' to "25"
      json_file:
        dest: /etc/file.conf
        key: 'foo'
        value: 25
        as_string: yes
```

This module supports all arguments supported by the [Ansible file](http://docs.ansible.com/ansible/file_module.html) module (like 'owner', 'group', 'mode' etcetera).

Acknowledgements
----------------

This library draws heavily from the [ini_file](http://docs.ansible.com/ansible/ini_file_module.html) core-module and @FauxFaux's [ghetto_json](https://github.com/FauxFaux/ansible-ghetto-json) library.

Limitations
-----------

`json_file` only works on files that are dictionaries (i.e. have a top-level '{').

Lists are not supported/tested

License
-------

MIT

Author Information
------------------

Pieter Lexis ([@lieter_](https://twitter.com/lieter_))
