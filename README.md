# CommunityTaxonomy
Curated Hierarchical Topic Taxonomy of Reddit Subreddits by initialized by posts on r/ListOfSubreddits. (currently 2900+ subreddits!)

Inside topics, each .txt file contains a list of subreddits which belong to that topic. Folders represent a subtopic with that topic (ex: 'Animals/Mammals/Cats.txt').

For ease of use in downstream applications, `merge_into_csv.py` will merge the folder structure into a csv where each row is a subreddit quantified by Primary, Secondary, Tertiary and Quaternary topics. (ex: `subreddit_taxonomy.csv`)

Contributors are welcome to expand this list!

## Current Taxonomy
```
topics
    │   Animals.txt
    │   NSFW.txt
    │   Technology.txt
    │
    ├───Animals
    │   │   Birds-General.txt
    │   │   Mammals-General.txt
    │   │
    │   └───Mammals
    │           Cats.txt
    │           Dogs.txt
    │
    ├───Discussion
    │   │   Advice-General.txt
    │   │   AMA-General.txt
    │   │   Games-General.txt
    │   │   General-General.txt
    │   │   Question_Answer-General.txt
    │   │   Stories-General.txt
    │   │   Support-General.txt
    │   │
    │   ├───Question_Answer
    │   │       Ask______.txt
    │   │
    │   └───Stories
    │           Customer Service.txt
    │           Revenge.txt
    │           Scary_Weird.txt
    │
    ├───Educational
    │   │   Anthropology-General.txt
    │   │   Art-General.txt
    │   │   Computer Science_Engineering-General.txt
    │   │   Economics-General.txt
    │   │   Educational-General.txt
    │   │   Environment-General.txt
    │   │   History-General.txt
    │   │   Language-General.txt
    │   │   Law-General.txt
    │   │   Math-General.txt
    │   │   Medicine-General.txt
    │   │   Psychology-General.txt
    │   │   Science-General.txt
    │   │
    │   ├───Art
    │   │       Painting.txt
    │   │       Reddit.txt
    │   │
    │   ├───Computer Science_Engineering
    │   │       Coding.txt
    │   │
    │   ├───Economics
    │   │       Business.txt
    │   │       Stocks.txt
    │   │
    │   ├───Educational
    │   │       Facts.txt
    │   │       Questions.txt
    │   │
    │   ├───History
    │   │       Historical Images.txt
    │   │
    │   └───Science
    │           Astronomy_Aliens.txt
    │           Biology.txt
    │           Chemistry.txt
    │           Physics.txt
    │
    ├───Entertainment
    │   │   Anime_Manga-General.txt
    │   │   Books_Writing-General.txt
    │   │   Celebrities-General.txt
    │   │   Cosplay-General.txt
    │   │   Games-General.txt
    │   │   General-General.txt
    │   │   Genres-General.txt
    │   │   Internet_Apps-General.txt
    │   │   Movies-General.txt
    │   │   Music-General.txt
    │   │   Sports-General.txt
    │   │   TV-General.txt
    │   │   Video games-General.txt
    │   │
    │   ├───Anime_Manga
    │   │       Individual Anime_manga.txt
    │   │
    │   ├───Books_Writing
    │   │       Comics.txt
    │   │       Individual books_stories_comics.txt
    │   │
    │   ├───Celebrities
    │   │       Individual Celebrities.txt
    │   │
    │   ├───Games
    │   │       Dungeons and Dragons.txt
    │   │       Magic.txt
    │   │
    │   ├───Genres
    │   │       Fantasy.txt
    │   │       Sci-fi.txt
    │   │
    │   ├───Internet_Apps
    │   │       4chan.txt
    │   │       Facebook.txt
    │   │       Internet Dating.txt
    │   │       Internet Politics.txt
    │   │       Live Streaming.txt
    │   │       Podcasts.txt
    │   │       Tumblr.txt
    │   │       Twitter.txt
    │   │       YouTube.txt
    │   │
    │   ├───Movies
    │   │       Individual Movies_Series.txt
    │   │
    │   ├───Music
    │   │       Artists.txt
    │   │       Genres.txt
    │   │       Instruments.txt
    │   │
    │   ├───Sports
    │   │       American Football.txt
    │   │       Baseball.txt
    │   │       Basketball.txt
    │   │       Boards.txt
    │   │       Cars.txt
    │   │       Fighting.txt
    │   │       Hockey.txt
    │   │       Olympics.txt
    │   │       Soccer.txt
    │   │
    │   ├───TV
    │   │       Individual Shows.txt
    │   │       Netflix Related.txt
    │   │
    │   └───Video games
    │           Deals.txt
    │           Game Systems_Consoles_Companies.txt
    │           Individual Video Games_Series.txt
    │
    ├───General Content
    │   │   Gifs-General.txt
    │   │   Images-General.txt
    │   │   Videos-General.txt
    │   │
    │   ├───Gifs
    │   │       People.txt
    │   │       Reaction.txt
    │   │       Science.txt
    │   │
    │   └───Images
    │           Images_Gifs of Women (SFW).txt
    │           Interesting.txt
    │           Photoshop.txt
    │           Redditors_Selfies.txt
    │           Wallpapers.txt
    │
    ├───Hobbies_Occupations
    │   │   Aquariums-General.txt
    │   │   Arts_Writing-General.txt
    │   │   Automotive-General.txt
    │   │   Design-General.txt
    │   │   Fake it til you make it-General.txt
    │   │   General-General.txt
    │   │   Job finding-General.txt
    │   │   Music-General.txt
    │   │   Outdoors-General.txt
    │   │   Photography_Film-General.txt
    │   │   Planes-General.txt
    │   │   Tech Related-General.txt
    │   │   Tools-General.txt
    │   │   Travel-General.txt
    │   │
    │   ├───Arts_Writing
    │   │       Writing.txt
    │   │
    │   ├───Automotive
    │   │       Car companies.txt
    │   │
    │   ├───Guns_Combat
    │   │       Combat.txt
    │   │       Guns.txt
    │   │
    │   ├───Outdoors
    │   │       Gardening.txt
    │   │       Hiking.txt
    │   │
    │   └───Tech Related
    │           Coding.txt
    │           PC Building.txt
    │           Tech Support.txt
    │
    ├───Humor
    │   │   General Humor-General.txt
    │   │   Memes_Rage comics-General.txt
    │   │
    │   ├───General Humor
    │   │       Jokes.txt
    │   │       Poor Quality or Bad Memes.txt
    │   │
    │   └───Memes_Rage comics
    │           Foreign.txt
    │           Memes.txt
    │           Other Memes.txt
    │           Rage Comics.txt
    │
    ├───Lifestyle
    │   │   Communities-General.txt
    │   │   Exercise_Health-General.txt
    │   │   Food-General.txt
    │   │   General-General.txt
    │   │   Money-General.txt
    │   │   Relationships_Sex-General.txt
    │   │   Religion_Beliefs-General.txt
    │   │   Self-Improvement-General.txt
    │   │
    │   ├───Communities
    │   │       Body_Diet.txt
    │   │       LGBT.txt
    │   │       Parenting.txt
    │   │
    │   ├───Drugs
    │   │       Alcohol.txt
    │   │       Marijuana.txt
    │   │       Other drugs.txt
    │   │
    │   ├───Exercise_Health
    │   │       Mental.txt
    │   │       Physical.txt
    │   │
    │   ├───Fashion_Beauty
    │   │       Body Image.txt
    │   │       Fashion.txt
    │   │
    │   ├───Food
    │   │       Cooking.txt
    │   │       Diets.txt
    │   │       Drinks (non-alcoholic).txt
    │   │       Recipes.txt
    │   │       Specific food.txt
    │   │
    │   ├───General
    │   │       Gender.txt
    │   │       Home.txt
    │   │
    │   ├───Money
    │   │       Betting_Investing_Stocks.txt
    │   │       Budget.txt
    │   │       Consumerism.txt
    │   │       CryptoCurrency.txt
    │   │
    │   ├───Relationships_Sex
    │   │       Family.txt
    │   │       Relationships.txt
    │   │       Sex.txt
    │   │
    │   └───Religion_Beliefs
    │           Atheism.txt
    │           Christianity.txt
    │           Philosophy.txt
    │
    ├───NSFW
    │   │   Asian-General.txt
    │   │   Ass-General.txt
    │   │   Athlete-General.txt
    │   │   Bikinis-General.txt
    │   │   Boobs_Nipples-General.txt
    │   │   Cam-General.txt
    │   │   Celebrity-General.txt
    │   │   Comics-General.txt
    │   │   Costumes-General.txt
    │   │   Cuck-General.txt
    │   │   Cum inside-General.txt
    │   │   Cum Location-General.txt
    │   │   Curvy_Thick_THICC-General.txt
    │   │   Dildos-General.txt
    │   │   Dresses_Skirts-General.txt
    │   │   Ebony-General.txt
    │   │   Face-General.txt
    │   │   Fit-General.txt
    │   │   Ginger-General.txt
    │   │   Gonewild-General.txt
    │   │   Hair-General.txt
    │   │   Hentai-General.txt
    │   │   Large Penis-General.txt
    │   │   Latina-General.txt
    │   │   Legs_feet-General.txt
    │   │   Looking for-General.txt
    │   │   MILF-General.txt
    │   │   Pants_Shorts-General.txt
    │   │   Petite-General.txt
    │   │   Positions-General.txt
    │   │   Professional_Cam-General.txt
    │   │   Pussy-General.txt
    │   │   Redditors-General.txt
    │   │   Skin-General.txt
    │   │   Snapchat-General.txt
    │   │   Social Media-General.txt
    │   │   Stockings_Socks-General.txt
    │   │   Teen-General.txt
    │   │   Trash-General.txt
    │   │   Underwear-General.txt
    │   │   Video Games-General.txt
    │   │   Waist_Tummy-General.txt
    │   │   Wet women-General.txt
    │   │   White-General.txt
    │   │   Wives-General.txt
    │   │
    │   ├───Asian
    │   │       Indian.txt
    │   │       Japanese.txt
    │   │       Korean.txt
    │   │
    │   ├───Ass
    │   │       Anal.txt
    │   │       Asshole.txt
    │   │       Yoga pants.txt
    │   │
    │   ├───Boobs_Nipples
    │   │       Busty.txt
    │   │       Nipples.txt
    │   │       Small.txt
    │   │       Titfuck.txt
    │   │
    │   ├───Gonewild
    │   │       Age.txt
    │   │       Couples.txt
    │   │       Curves.txt
    │   │       Ethnicity.txt
    │   │       Occupation.txt
    │   │
    │   ├───Legs_feet
    │   │       Feet.txt
    │   │       Thighs.txt
    │   │
    │   ├───Pants_Shorts
    │   │       Yoga pants.txt
    │   │
    │   ├───Pussy
    │   │       Mound.txt
    │   │
    │   ├───Social Media
    │   │       OnlyFans.txt
    │   │       TikTok.txt
    │   │
    │   └───Underwear
    │           Thongs.txt
    │
    ├───Other
    │   │   Conspiracy-General.txt
    │   │   Cringe-General.txt
    │   │   Cute-General.txt
    │   │   Disgusting_Angering_Scary_Weird-General.txt
    │   │   Free Stuff-General.txt
    │   │   General-General.txt
    │   │   Geography-General.txt
    │   │   Hold My ____-General.txt
    │   │   Meta-General.txt
    │   │   Mind blowing-General.txt
    │   │   Nature-General.txt
    │   │   Nostalgia_Time-General.txt
    │   │   Parodies-General.txt
    │   │   SFWPorn Network-General.txt
    │   │   Shitty-General.txt
    │   │   Unexpected-General.txt
    │   │   Visually Appealing-General.txt
    │   │   Weird Feelings_Categorize Later-General.txt
    │   │
    │   ├───Cringe
    │   │       Called out.txt
    │   │       Neckbeard.txt
    │   │
    │   ├───Disgusting_Angering_Scary_Weird
    │   │       Angering.txt
    │   │       Cursed.txt
    │   │       Edgy.txt
    │   │       Judgy.txt
    │   │       Scary (potentially NSFL).txt
    │   │
    │   ├───Gender
    │   │       For Men.txt
    │   │       For Women.txt
    │   │
    │   ├───General
    │   │       Looking for something.txt
    │   │
    │   ├───Geography
    │   │       Africa.txt
    │   │       Asia.txt
    │   │       Europe.txt
    │   │       North America.txt
    │   │       Oceania.txt
    │   │       South America.txt
    │   │
    │   ├───Meta
    │   │       Administrative.txt
    │   │       Apps.txt
    │   │       Circlejerks.txt
    │   │       Drama.txt
    │   │       Negative.txt
    │   │       Positive.txt
    │   │       Subreddits.txt
    │   │
    │   ├───Nature
    │   │       Plants_Fungi.txt
    │   │       Violent Nature.txt
    │   │       Weather.txt
    │   │
    │   └───News_Politics
    │           News.txt
    │           Politics.txt
    │
    └───Technology
        │   3D Printing-General.txt
        │   Business Tech-General.txt
        │   Data-General.txt
        │   Digital Currency-General.txt
        │   Programming-General.txt
        │   Sound-General.txt
        │
        └───Business Tech
                Android products.txt
                Apple Products.txt
                Gadgets.txt
                Google Products.txt
                Linux.txt
                Microsoft Products.txt
```