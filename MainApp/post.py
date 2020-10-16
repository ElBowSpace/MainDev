from .models import Post


def add_post(body, time_stamp, user, reply=None, image=None):
    new_post = Post.objects.create(reply=reply,
                                   body=body,
                                   time_stamp=time_stamp,
                                   image=image,
                                   user=user)
    new_post.save()
    return new_post


def edit_post(post_id, new_body=None):
    revised_post = Post.objects.get(id=post_id)
    if new_body is not None:
        revised_post.body = new_body
    revised_post.save()

def get_post(post_id):
    return Post.objects.get(id=post_id)

def get_all_posts():
    return Post.objects.all()

def delete_post(post_id):
    return Post.objects.get(id=post_id).delete()
