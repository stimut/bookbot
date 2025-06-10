
def count_words(text):
    return len(text.split())


def count_chars(text):
    freq = {}
    for ch in text:
        lower_ch = ch.lower()
        if lower_ch not in freq:
            freq[lower_ch] = 0

        freq[lower_ch] += 1

    return freq


def sort_freq(ch_freq):
    freq_list = []
    for ch in ch_freq:
        freq_list.append({"char": ch, "num": ch_freq[ch]})
    freq_list = [{"char": ch, "num": ch_freq[ch]} for ch in ch_freq]

    def sort_key(item):
        return item["num"]
    freq_list.sort(reverse=True, key=sort_key)

    return freq_list
