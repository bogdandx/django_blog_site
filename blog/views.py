from django.shortcuts import render
from datetime import date

all_posts = [
    {
      "slug": "hike-in-the-mountains",
      "image": "mountains.jpg",
      "author": "Bogdan",
      "date": date(2023, 6, 18),
      "title": "Mountain Hiking",
      "excerpt": """
          There's nothing like the views you get when hiking in the mountains! 
          And I wasn't even prepared for what happened whilst I was enjoying the view!""",
      "content": """
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Modi nobis nulla pariatur
            temporibus? Aspernatur blanditiis debitis dolorum eius ex in ipsum laboriosam odio
            perspiciatis tempore. Culpa ex officiis quidem saepe.
            
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Modi nobis nulla pariatur
            temporibus? Aspernatur blanditiis debitis dolorum eius ex in ipsum laboriosam odio
            perspiciatis tempore. Culpa ex officiis quidem saepe.
            
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Modi nobis nulla pariatur
            temporibus? Aspernatur blanditiis debitis dolorum eius ex in ipsum laboriosam odio
            perspiciatis tempore. Culpa ex officiis quidem saepe."""},
    {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "Bogdan",
        "date": date(2022, 5, 1),
        "title": "Programming Is Great!",
        "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
        "content": """
      Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
      aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
      velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

      Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
      aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
      velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

      Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
      aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
      velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
    """
    },
{
        "slug": "into-the-woods",
        "image": "woods.jpg",
        "author": "Bogdan",
        "date": date(2020, 8, 5),
        "title": "Nature At Its Best",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    }
]

def get_date(post):
    return post['date']
def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:] # blast 3 items
    return render(request, "blog/index.html", {"posts": latest_posts})

def posts(request):
    return render(request, "blog/all-posts.html", {"all_posts": all_posts})

def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {"post": identified_post})
