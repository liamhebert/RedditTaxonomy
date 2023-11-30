from glob import glob
import pandas as pd

def merge_into_csv(data, files, level=0):
    for file in files:
        catagories = file.strip('.txt').split('\\')
        print(file)
        primary = catagories[1]
        secondary = catagories[2] if len(catagories) > 2 else 'NA'
        tertiary = catagories[3] if len(catagories) > 3 else 'NA'
        quadternary = catagories[4] if len(catagories) > 4 else 'NA'
        with open(file, 'r') as read:
            for line in read:
                line = line.strip('\n')
                data['subreddit'] += [line]
                data['primary'] += [primary]
                data['secondary'] += [secondary]
                data['tertiary'] += [tertiary]
                data['quadternary'] += [quadternary]
            
    
def main():
    data = {
        'subreddit': [],
        'primary': [],
        'secondary': [],
        'tertiary': [],
        'quadternary': []
    }
    merge_into_csv(data, list(glob('topics/*.txt')) + list(glob('topics/*/*.txt')) + list(glob('topics/*/*/*.txt')) + list(glob('topics/*/*/*/*.txt')))
    data = pd.DataFrame(data).to_csv('subreddit_taxonomy.csv')
    

if __name__ == '__main__':
    main()