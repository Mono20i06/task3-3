def input_a_sentence() -> str:
    s = input('Введите предложение из двух слов: ')
    return s


def extract_words(s: str) -> list:
    w = s.split(' ')
    assert len(w) == 2, f"error! sentence '{s}' contains"
    return w


def render_template(t: str, c: dict) -> str:
    r = t.format(**c)
    return r


def main():
    sentence = input_a_sentence()
    words = extract_words(sentence)

    template = '!{word2} {word1}!'
    context = {
        'word1': words[0],
        'word2': words[1],
    }
    
    result = render_template(template, context)

    return result


if __name__ == '__main__':
    print(main())
