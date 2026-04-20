1. Data - I was able to run an X/Twitter scraping API for tweets between January 2025 and today, mainly focusing on keywords related to FAA staffing and safety, air traffic control shortages and understaffing, LaGuardia crash/collision discussions, aviation oversight and reform, and FAA-related delay concerns. I picked this time window because it better matches the current policy context we were trying to motivate in the proposal. I’m happy to send over the JSON/CSV once the scraping is completed, but on first glance, it looks like we are getting tweets from politicians, the FAA itself, news outlets, and civilians tied directly to recent safety concerns and staffing shortages. My thought is that this newer dataset would give us a more recent and policy-relevant source to work with, especially compared with relying only on the 2015 Twitter dataset. With the number of tokens I’m able to use, we should be able to get a dataset of a little over 4,300 tweets, which I hope should be sufficient. The exported data include tweet-level fields such as the tweet ID, URL, text, timestamp, engagement counts, language, and reply/quote indicators. In particular, the text field would remain the main focus of the analysis.

Tweet ID (id): unique identifier for each tweet
Tweet URL (url): direct link to the tweet on X/Twitter
Content (text): the actual text of the tweet; this will be the main focus of our analysis
Created At (createdAt): timestamp showing when the tweet was posted
Profile Picture (author.profilePicture): profile image URL of the tweet’s author
Retweets (retweetCount): number of retweets the tweet received
Replies (replyCount): number of replies to the tweet
Likes (likeCount): number of likes the tweet received
Quotes (quoteCount): number of quote tweets the tweet received
Views (viewCount): number of views on the tweet
Bookmarks (bookmarkCount): number of times the tweet was bookmarked
Source (source): platform or client used to post the tweet, if available
Language (lang): detected language of the tweet
Is Reply (isReply): indicator for whether the tweet is a reply
Is Quote (isQuote): indicator for whether the tweet is a quote tweet
Is Pinned (isPinned): indicator for whether the tweet is pinned on the author’s profile

Admittedly, the 2015 Twitter dataset is still cleaner and easier to work with, since it is a well-known Kaggle dataset that has been analyzed extensively before. I was also able to run some basic sentiment and n-gram analysis on it already, and the results were clean and interpretable. Because of that, I think it still works well as a proof-of-concept, and we could try to mirror similar techniques on this newer dataset. That would also give us a chance to compare the two datasets directly and see whether similar complaint themes or language patterns show up across both.

Private airlines may not always be fully forthcoming about operational or budget decisions that could affect safety and service. Public social media discussion may therefore offer a more direct view of how passengers are experiencing these issues. I do not mean that social media would replace formal evidence, but rather that it could help point to patterns that agencies like the FAA may want to watch more closely.
