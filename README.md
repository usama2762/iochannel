# IO Channel

### Install

```bash
pip install git+https://github.com/aixplain/io_channel.git#egg=io_channel
```

### Use

```python
from io_channel import IOChannel
# request_id is a uuid4 string
request_id = 'uuid4'
IOChannel().read_input(request_id)
```
