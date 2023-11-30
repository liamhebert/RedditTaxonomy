# Reddit Taxonomy
Curated Hierarchical Topic Taxonomy of Reddit Subreddits by initialized by posts on r/ListOfSubreddits. (currently 2900+ subreddits!)

Inside topics, each .txt file contains a list of subreddits which belong to that topic. Folders represent a subtopic with that topic (ex: `Animals/Mammals/Cats.txt` for cat-oriented subreddits).

For ease of use in downstream applications, `merge_into_csv.py` will merge the folder structure into a csv where each row is a subreddit quantified by Primary, Secondary, Tertiary and Quaternary topics. (ex: `subreddit_taxonomy.csv`)

Contributors are welcome to expand this list!
