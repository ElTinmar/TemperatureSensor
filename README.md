# TemperatureSensor

read from DS18B20 with arduino

## install

Upload sketch to Arduino. Make sure to use a 4.7k Ohm pull-up resistor
between signal and +5V.

```bash
pip install ds18b20@git+https://github.com/ElTinmar/TemperatureSensor.git
```

## use

```python
from ds18b20 import read_temperature_celsius
read_temperature_celsius()
```
