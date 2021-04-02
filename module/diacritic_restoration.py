import keras
import numpy as np
import json


def load_json_data(filename):
    with open(filename, 'rb') as fr:
        samples = json.load(fr)
        fr.close()
    return samples


def write_json_data(filename, data):
    with open(filename, 'wb') as fw:
        data = json.dumps(data, indent=2, ensure_ascii=False).encode('utf-8')
        fw.write(data)
        fw.close()
    return True


model = keras.models.load_model('/Users/LongNH/Workspace/norm-text-demo/flash_back/model/model16')

input_token_index = load_json_data('/Users/LongNH/Workspace/norm-text-demo/flash_back/model/input_char1.json')
num_encoder_tokens = len(input_token_index.keys())

target_token_index = load_json_data('/Users/LongNH/Workspace/norm-text-demo/flash_back/model/target_char1.json')
reverse_target_char_index = dict((i, char) for char, i in target_token_index.items())


def gen_sequence(input_seq):
    input_sent = [input_token_index[char] if char in input_token_index else num_encoder_tokens for char in input_seq]
    input_sent = keras.utils.to_categorical([input_sent], num_classes=num_encoder_tokens+1)
    pred = model.predict(input_sent)[0]
    pred = [np.argmax(p) for p in pred]
    for i in range(len(pred)):
        if pred[i] in reverse_target_char_index:
            pred[i] = reverse_target_char_index[pred[i]]
        else:
            pred[i] = input_seq[i]

    return "".join(pred)


# print(gen_sequence('Vao mot ngay khong xa, chung ta se gap lai nhau'))


