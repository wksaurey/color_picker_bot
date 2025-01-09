import praw

reddit = praw.Reddit('color_picker_bot_creds')

if not reddit.read_only:
    print(f'Initialized u//color_picker_bot with write permissions')

subreddit = reddit.subreddit('test')

print(f'Listening to {subreddit.display_name} comment stream')
for comment in subreddit.stream.comments():
    if 'u/color_picker_bot' in comment.body:
        comment.reply('Hello, I am a bot!')
        print(f'Replied to comment {comment.id}')