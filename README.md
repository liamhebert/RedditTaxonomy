# Reddit Taxonomy
Curated Hierarchical Topic Taxonomy of Reddit Subreddits by initialized by posts on r/ListOfSubreddits. (currently 2900+ subreddits!)

Inside topics, each .txt file contains a list of subreddits which belong to that topic. Folders represent a subtopic within that topic (ex: `Animals/Mammals/Cats.txt` for cat-oriented subreddits).

For ease of use in downstream applications, `merge_into_csv.py` will merge the folder structure into a csv where each row is a subreddit quantified by Primary, Secondary, Tertiary and Quaternary topics. (ex: `subreddit_taxonomy.csv`)

Contributors are welcome to expand this list!

## Current Taxonomy
```
└───topics
    ├───Animals
    │   │   Birds.txt
    │   │   Mammals.txt
    │   │   NA.txt
    │   │
    │   └───Mammals
    │       │   Cats.txt
    │       │   Dogs.txt
    │       │
    │       └───Dogs
    │               Breeds.txt
    │
    ├───Discussion
    │   │   Advice.txt
    │   │   AMA.txt
    │   │   Games.txt
    │   │   General.txt
    │   │   Question_Answer.txt
    │   │   Stories.txt
    │   │   Support.txt
    │   │
    │   ├───Question_Answer
    │   │   │   Ask______.txt
    │   │   │
    │   │   └───Ask______
    │   │           Occupation.txt
    │   │           Sex_Gender.txt
    │   │
    │   └───Stories
    │           Customer Service.txt
    │           Revenge.txt
    │           Scary_Weird.txt
    │
    ├───Educational
    │   │   Anthropology.txt
    │   │   Art.txt
    │   │   Computer Science_Engineering.txt
    │   │   Economics.txt
    │   │   Educational.txt
    │   │   Environment.txt
    │   │   History.txt
    │   │   Language.txt
    │   │   Law.txt
    │   │   Math.txt
    │   │   Medicine.txt
    │   │   Psychology.txt
    │   │   Science.txt
    │   │
    │   ├───Art
    │   │       Painting.txt
    │   │       Reddit.txt
    │   │
    │   ├───Computer Science_Engineering
    │   │   │   Coding.txt
    │   │   │
    │   │   └───Coding
    │   │           Python.txt
    │   │
    │   ├───Economics
    │   │       Business.txt
    │   │       Stocks.txt
    │   │
    │   ├───Educational
    │   │   │   Facts.txt
    │   │   │   Questions.txt
    │   │   │
    │   │   └───Questions
    │   │           Explain Like....txt
    │   │
    │   ├───History
    │   │       Historical Images.txt
    │   │
    │   └───Science
    │       │   Astronomy_Aliens.txt
    │       │   Biology.txt
    │       │   Chemistry.txt
    │       │   Physics.txt
    │       │
    │       └───Astronomy_Aliens
    │               Companies.txt
    │
    ├───Entertainment
    │   │   Anime_Manga.txt
    │   │   Books_Writing.txt
    │   │   Celebrities.txt
    │   │   Cosplay.txt
    │   │   Games.txt
    │   │   General.txt
    │   │   Genres.txt
    │   │   Internet_Apps.txt
    │   │   Movies.txt
    │   │   Music.txt
    │   │   Sports.txt
    │   │   TV.txt
    │   │   Video games.txt
    │   │
    │   ├───Anime_Manga
    │   │       Individual Anime_manga.txt
    │   │
    │   ├───Books_Writing
    │   │   │   Comics.txt
    │   │   │   Individual books_stories_comics.txt
    │   │   │
    │   │   └───Individual books_stories_comics
    │   │           Game of Thrones.txt
    │   │           Lord of the Rings.txt
    │   │
    │   ├───Celebrities
    │   │   └───Individual Celebrities
    │   │           Female.txt
    │   │           Male.txt
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
    │   │   │   4chan.txt
    │   │   │   Facebook.txt
    │   │   │   Internet Dating.txt
    │   │   │   Internet Politics.txt
    │   │   │   Live Streaming.txt
    │   │   │   Podcasts.txt
    │   │   │   Tumblr.txt
    │   │   │   Twitter.txt
    │   │   │   YouTube.txt
    │   │   │
    │   │   └───YouTube
    │   │           Individual YouTubers_Companies.txt
    │   │           Pewdiepie.txt
    │   │           Roosterteeth.txt
    │   │
    │   ├───Movies
    │   │   │   Individual Movies_Series.txt
    │   │   │
    │   │   └───Individual Movies_Series
    │   │           Comic movies.txt
    │   │
    │   ├───Music
    │   │   │   Artists.txt
    │   │   │   Genres.txt
    │   │   │   Instruments.txt
    │   │   │
    │   │   └───Genres
    │   │           Electronic.txt
    │   │           Hip Hop.txt
    │   │           Metal.txt
    │   │           Pop.txt
    │   │
    │   ├───Sports
    │   │   │   American Football.txt
    │   │   │   Baseball.txt
    │   │   │   Basketball.txt
    │   │   │   Boards.txt
    │   │   │   Cars.txt
    │   │   │   Fighting.txt
    │   │   │   Hockey.txt
    │   │   │   Olympics.txt
    │   │   │   Soccer.txt
    │   │   │
    │   │   ├───American Football
    │   │   │       American Football Teams.txt
    │   │   │
    │   │   ├───Basketball
    │   │   │       Teams.txt
    │   │   │
    │   │   └───Soccer
    │   │           Soccer Teams.txt
    │   │
    │   ├───TV
    │   │   │   Individual Shows.txt
    │   │   │   Netflix Related.txt
    │   │   │
    │   │   └───Individual Shows
    │   │           Animated.txt
    │   │           Doctor Who.txt
    │   │           Dragon Ball Z.txt
    │   │           It's Always Sunny in Philadelphia.txt
    │   │           Seinfeld.txt
    │   │
    │   └───Video games
    │       │   Deals.txt
    │       │   Game Systems_Consoles_Companies.txt
    │       │   Individual Video Games_Series.txt
    │       │
    │       ├───Game Systems_Consoles_Companies
    │       │       Nintendo.txt
    │       │       PC.txt
    │       │       Sony.txt
    │       │       
    │       └───Individual Video Games_Series
    │               Animal Crossing.txt
    │               Borderlands.txt
    │               Dark Souls.txt
    │               Destiny.txt
    │               Diablo.txt
    │               Elder Scrolls.txt
    │               Fallout.txt
    │               Fire Emblem.txt
    │               First Person Shooters (fps).txt
    │               Fortnite.txt
    │               Grand Theft Auto (GTA).txt
    │               Hearthstone.txt
    │               League of Legends.txt
    │               Minecraft.txt
    │               MMOs.txt
    │               Overwatch.txt
    │               Pokemon.txt
    │               PUBG.txt
    │               Red Dead Redemption.txt
    │               Rocket League.txt
    │               Runescape.txt
    │               Sports.txt
    │               Witcher.txt
    │               Zelda.txt
    │
    ├───General Content
    │   │   Gifs.txt
    │   │   Images.txt
    │   │   Videos.txt
    │   │
    │   ├───Gifs
    │   │   │   People.txt
    │   │   │   Reaction.txt
    │   │   │   Science.txt
    │   │   │
    │   │   └───Science
    │   │           Nature.txt
    │   │
    │   └───Images
    │       │   Images_Gifs of Women (SFW).txt
    │       │   Interesting.txt
    │       │   Photoshop.txt
    │       │   Redditors_Selfies.txt
    │       │   Wallpapers.txt
    │       │
    │       └───Images_Gifs of Women (SFW)
    │               Asian.txt
    │
    ├───Hobbies_Occupations
    │   │   Aquariums.txt
    │   │   Arts_Writing.txt
    │   │   Automotive.txt
    │   │   Design.txt
    │   │   Fake it til you make it.txt
    │   │   General.txt
    │   │   Job finding.txt
    │   │   Music.txt
    │   │   Outdoors.txt
    │   │   Photography_Film.txt
    │   │   Planes.txt
    │   │   Tech Related.txt
    │   │   Tools.txt
    │   │   Travel.txt
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
    │   │   General Humor.txt
    │   │   Memes_Rage comics.txt
    │   │
    │   ├───General Humor
    │   │       Jokes.txt
    │   │       Poor Quality or Bad Memes.txt
    │   │
    │   └───Memes_Rage comics
    │       │   Foreign.txt
    │       │   Memes.txt
    │       │   Other Memes.txt
    │       │   Rage Comics.txt
    │       │
    │       └───Memes
    │               Anime.txt
    │               ____irl.txt
    │
    ├───Lifestyle
    │   │   Communities.txt
    │   │   Exercise_Health.txt
    │   │   Food.txt
    │   │   General.txt
    │   │   Money.txt
    │   │   Relationships_Sex.txt
    │   │   Religion_Beliefs.txt
    │   │   Self-Improvement.txt
    │   │
    │   ├───Communities
    │   │   │   Body_Diet.txt
    │   │   │   LGBT.txt
    │   │   │   Parenting.txt
    │   │   │
    │   │   └───LGBT
    │   │           Transgender.txt
    │   │
    │   ├───Drugs
    │   │   │   Alcohol.txt
    │   │   │   Marijuana.txt
    │   │   │   Other drugs.txt
    │   │   │
    │   │   └───Alcohol
    │   │           Beer.txt
    │   │
    │   ├───Exercise_Health
    │   │   │   Mental.txt
    │   │   │   Physical.txt
    │   │   │
    │   │   └───Physical
    │   │           Diet.txt
    │   │           Exercise.txt
    │   │           Keto.txt
    │   │           Lifting_Weights.txt
    │   │           Medicine_Disease.txt
    │   │           Progress Pictures.txt
    │   │           Running.txt
    │   │           Weight_Body Shape Control.txt
    │   │
    │   ├───Fashion_Beauty
    │   │   │   Body Image.txt
    │   │   │   Fashion.txt
    │   │   │
    │   │   ├───Body Image
    │   │   │       Hair.txt
    │   │   │       Tattoos.txt
    │   │   │
    │   │   └───Fashion
    │   │           Shoes.txt
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
    │   │   │   Family.txt
    │   │   │   Relationships.txt
    │   │   │   Sex.txt
    │   │   │
    │   │   └───Relationships
    │   │           Online Relationships.txt
    │   │
    │   └───Religion_Beliefs
    │           Atheism.txt
    │           Christianity.txt
    │           Philosophy.txt
    │
    ├───NSFW
    │   │   Asian.txt
    │   │   Ass.txt
    │   │   Athlete.txt
    │   │   Bikinis.txt
    │   │   Boobs_Nipples.txt
    │   │   Cam.txt
    │   │   Celebrity.txt
    │   │   Comics.txt
    │   │   Costumes.txt
    │   │   Cuck.txt
    │   │   Cum inside.txt
    │   │   Cum Location.txt
    │   │   Curvy_Thick_THICC.txt
    │   │   Dildos.txt
    │   │   Dresses_Skirts.txt
    │   │   Ebony.txt
    │   │   Face.txt
    │   │   Fit.txt
    │   │   Ginger.txt
    │   │   Gonewild.txt
    │   │   Hair.txt
    │   │   Hentai.txt
    │   │   Large Penis.txt
    │   │   Latina.txt
    │   │   Legs_feet.txt
    │   │   Looking for.txt
    │   │   MILF.txt
    │   │   NA.txt
    │   │   Pants_Shorts.txt
    │   │   Petite.txt
    │   │   Positions.txt
    │   │   Professional_Cam.txt
    │   │   Pussy.txt
    │   │   Redditors.txt
    │   │   Skin.txt
    │   │   Snapchat.txt
    │   │   Social Media.txt
    │   │   Stockings_Socks.txt
    │   │   Teen.txt
    │   │   Trash.txt
    │   │   Underwear.txt
    │   │   Video Games.txt
    │   │   Waist_Tummy.txt
    │   │   Wet women.txt
    │   │   White.txt
    │   │   Wives.txt
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
    │   │   Conspiracy.txt
    │   │   Cringe.txt
    │   │   Cute.txt
    │   │   Disgusting_Angering_Scary_Weird.txt
    │   │   Free Stuff.txt
    │   │   General.txt
    │   │   Geography.txt
    │   │   Hold My ____.txt
    │   │   Meta.txt
    │   │   Mind blowing.txt
    │   │   Nature.txt
    │   │   Nostalgia_Time.txt
    │   │   Parodies.txt
    │   │   SFWPorn Network.txt
    │   │   Shitty.txt
    │   │   Unexpected.txt
    │   │   Visually Appealing.txt
    │   │   Weird Feelings_Categorize Later.txt
    │   │
    │   ├───Cringe
    │   │   │   Called out.txt
    │   │   │   Neckbeard.txt
    │   │   │
    │   │   └───Neckbeard
    │   │           Girls.txt
    │   │           I Am Very.txt
    │   │           Neckbeard.txt
    │   │           Parents.txt
    │   │
    │   ├───Disgusting_Angering_Scary_Weird
    │   │   │   Angering.txt
    │   │   │   Cursed.txt
    │   │   │   Edgy.txt
    │   │   │   Judgy.txt
    │   │   │   Scary (potentially NSFL).txt
    │   │   │
    │   │   ├───Cursed
    │   │   │       Blessed.txt
    │   │   │
    │   │   └───Scary (potentially NSFL)
    │   │           Creepy.txt
    │   │           Imaginary.txt
    │   │           Water is scary.txt
    │   │
    │   ├───Gender
    │   │       For Men.txt
    │   │       For Women.txt
    │   │
    │   ├───General
    │   │       Looking for something.txt
    │   │
    │   ├───Geography
    │   │   │   Africa.txt
    │   │   │   Asia.txt
    │   │   │   Europe.txt
    │   │   │   Oceania.txt
    │   │   │   South America.txt
    │   │   │
    │   │   ├───Asia
    │   │   │       Japan.txt
    │   │   │       Korea.txt
    │   │   │
    │   │   ├───Europe
    │   │   │       France.txt
    │   │   │       Germany.txt
    │   │   │       Russia.txt
    │   │   │       Sweden.txt
    │   │   │       United Kingdom.txt
    │   │   │
    │   │   └───North America
    │   │           California.txt
    │   │           Canada.txt
    │   │           Colorado.txt
    │   │           Florida.txt
    │   │           Mexico.txt
    │   │           Texas.txt
    │   │           USA
    │   │           Washington.txt
    │   │
    │   ├───Meta
    │   │   │   Administrative.txt
    │   │   │   Apps.txt
    │   │   │   Circlejerks.txt
    │   │   │   Drama.txt
    │   │   │   Negative.txt
    │   │   │   Positive.txt
    │   │   │   Subreddits.txt
    │   │   │
    │   │   ├───Administrative
    │   │   │       April Fools.txt
    │   │   │
    │   │   └───Subreddits
    │   │           Moderating.txt
    │   │           Subreddit Simulator.txt
    │   │
    │   ├───Nature
    │   │       Plants_Fungi.txt
    │   │       Violent Nature.txt
    │   │       Weather.txt
    │   │
    │   └───News_Politics
    │       │   News.txt
    │       │   Politics.txt
    │       │
    │       ├───News
    │       │       Fake News.txt
    │       │
    │       └───Politics
    │               Alt-Right.txt
    │               Anti-Trump.txt
    │               Capitalism.txt
    │               Gender Politics.txt
    │               Left.txt
    │
    └───Technology
        │   3D Printing.txt
        │   Business Tech.txt
        │   Data.txt
        │   Digital Currency.txt
        │   NA.txt
        │   Programming.txt
        │   Sound.txt
        │
        └───Business Tech
            │   Android products.txt
            │   Apple Products.txt
            │   Gadgets.txt
            │   Google Products.txt
            │   Linux.txt
            │   Microsoft Products.txt
            │
            └───Gadgets
                    Hardware.txt
                    Kodi.txt
```
