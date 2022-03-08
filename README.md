# ehuatuo [![Version][version-badge]][version-link] ![MIT License][license-badge]


Add ehuatuo effect to image


`ehuatuo` 是一个提供医疗命名实体识别服务的库


### 使用python进行测试：
```
import huatuo

sentence = '没有及时的盖被子，都会导致感冒的情况发生，下面我们一起了解下热感冒了吃什么好的快吧！风热感冒常伴有内火患者会出现咳嗽以及嗓子痒痛，在药物治疗的饿同时可以患者可以适当的吃冰糖雪梨茶，冰糖雪梨能够有效的去火，缓解患者因咽喉肿痛引起的咳嗽嗓子疼痛症状'

ner_result = huatuo.diagnosis(sentence)
```

运行以上脚本输出结果：
```
[{'start_idx': 13, 'end_idx': 14, 'type': 'disease', 'entity': '感冒'},
{'start_idx': 31, 'end_idx': 32, 'type': 'disease', 'entity': '感冒'},
{'start_idx': 44, 'end_idx': 45, 'type': 'disease', 'entity': '感冒'},
{'start_idx': 42, 'end_idx': 45, 'type': 'disease', 'entity': '风热感冒'},
{'start_idx': 56, 'end_idx': 57, 'type': 'disease', 'entity': '咳嗽'},
{'start_idx': 62, 'end_idx': 62, 'type': 'symptom', 'entity': '痒'},
{'start_idx': 62, 'end_idx': 63, 'type': 'disease', 'entity': '痒痛'},
{'start_idx': 84, 'end_idx': 85, 'type': 'food', 'entity': '冰糖'},
{'start_idx': 84, 'end_idx': 87, 'type': 'food', 'entity': '冰糖雪梨'},
{'start_idx': 87, 'end_idx': 87, 'type': 'food', 'entity': '梨'},
{'start_idx': 84, 'end_idx': 88, 'type': 'food', 'entity': '冰糖雪梨茶'},
{'start_idx': 90, 'end_idx': 91, 'type': 'food', 'entity': '冰糖'},
{'start_idx': 90, 'end_idx': 93, 'type': 'food', 'entity': '冰糖雪梨'},
{'start_idx': 93, 'end_idx': 93, 'type': 'food', 'entity': '梨'},
{'start_idx': 107, 'end_idx': 110, 'type': 'symptom', 'entity': '咽喉肿痛'},
{'start_idx': 114, 'end_idx': 115, 'type': 'disease', 'entity': '咳嗽'},
{'start_idx': 118, 'end_idx': 119, 'type': 'disease', 'entity': '疼痛'},
{'start_idx': 120, 'end_idx': 121, 'type': 'disease', 'entity': '症状'}]
```

### 使用方式

```
usage: ehuatuo [-h] [--sentence TEXT_OF_SENTENCE] [--out NERRESULT]

optional arguments:
  -h, --help         show this help message and exit
  --sentence TEXT_OF_SENTENCE  sentence with medical information
  --out NERRESULT     ner result
```


### 安装

```
$ pip install huatuo
```


### License

[MIT](https://github.com/easonforai/huatuo/blob/master/LICENSE)


[version-badge]:   https://img.shields.io/badge/version-0.1-brightgreen.svg
[version-link]:    https://pypi.python.org/pypi/huatuo/
[license-badge]:   https://img.shields.io/github/license/pythonml/huatuo.svg
