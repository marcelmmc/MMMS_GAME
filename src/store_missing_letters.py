df = pd.read_csv('../data/mock2.csv')
missing_keys = df.iloc[2].value
cleaned_string = re.sub(r'[^a-zA-Z0-9]', ' ', missing_keys)
freq_keys = dict()

missing_keys_arr = cleaned_string.split()
for k in freq_keys.keys():
    freq_keys[k] = freq_keys[k] - 1 if freq_keys[k] > 0 else 0

for i in missing_keys_arr:
    if not (i in freq_keys):
        freq_keys[i] = 1
    else:
        freq_keys[i] += 1

with open('missing_keys.pkl','wb') as f:
    pickle.dump(freq_keys, f)