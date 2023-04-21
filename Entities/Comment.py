class Comment:
    def __init__(self, url, comment_index, post_index, politician,comment_type):
        self.comment_url=url
        if comment_type=='regular-comment':
            self.comment_id = url.split('comment_id=')[1]
        else:
            self.comment_id=url.split('&reply_comment_id=')[1]
        self.comment_index = comment_index
        self.post_index = post_index
        self.politician = politician
        self.comment_type=comment_type
    def __str__(self):
        return f'{self.comment_id},{self.comment_index},{self.post_index},{self.politician}\n'
