## Python finite state machine

### Create a FSM object with default state:
```python 
from fsm import FSM

fsm_obj = FSM(default='default_state')
```

### Initialize the value, or not:
```python
fsm_obj.init_state('some_state')
print(fsm_obj.get_state('some_state')) # default_state
```

### Set the value you want:
```python
fsm_obj.set_state('some_state', 'some_value')
print(fsm_obj.get_state('some_state')) # some_value
```

### Create a state object with many fields:
```python
fsm_obj.add_extra_state('some_state', 'some_name', 'some_info')
fsm_obj.add_extra_state('some_state', 'some_second_name', 'some_second_info')
all_states = fsm_obj.all_extra_states('some_state')
print(all_states.some_name, all_states.some_second_name) # some_info some_second_info
```

### Create a state with a lifetime:
```python
fsm_obj.set_expired('some_key', 3) # time in seconds
```
* Let's see what happened:
```python
import time

while True:
    print(fsm_obj.check_expired('some_key'))
    time.sleep(1)
```
* Output:
```
0:00:03
0:00:02
0:00:01
False
```
