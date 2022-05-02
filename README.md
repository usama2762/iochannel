# IO Channel

### Install

```bash
pip install -e git+https://github.com/aixplain/iochannel.git#egg=iochannel
```

### Use

```python
from iochannel import IOChannel
# request_id is a uuid4 string
request_id = 'uuid4'
IOChannel().read_input(request_id)
```
