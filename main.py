import json
import sys
import os
import argparse

package_path = os.path.dirname(os.path.abspath(__file__)) + '/'
sys.path.append(package_path)
sys.path.append(package_path + 'preprocess/')
sys.path.append(package_path + 'models/RNN/')
sys.path.append(package_path + 'models/LDA/')

from word_vector import WordVector
from word_recomm import WordRecommendor


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='model runner')
    parser.add_argument('--mode', default='recommend', help='choose the action train/recommend')
    parser.add_argument('--model', default='LDA', help='choose the model LDA/RNN')
    parser.add_argument('--word', default='google', help='your input word for recommendation')
    args = parser.parse_args()

    with open(package_path + 'config.json', 'r', encoding='utf8') as f:
        config = json.load(f)

    if args.mode == 'train':
        word_vector = WordVector(args.model)
        word_vector.train(config)

    elif args.mode == 'recommend':
        recomm = WordRecommendor(args.model)
        result = recomm.get_top_words(args.word)
        print(result)
