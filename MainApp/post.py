from .models import Post


def add_post(body, time_stamp, user, reply=None, image=None):
    new_post = Post.objects.create(reply=reply,
                                   body=body,
                                   time_stamp=time_stamp,
                                   image=image,
                                   user=user)
    new_post.save()
    return new_post
