title: Getting a machine to understand chicken breeds
summary: 
slug: machine-learning-chickens
category: Machine Learning
tags: ai, machine learning, deep learning
date: 2022-09-04

<figure class="image-container image-right">
    <img class="article-image" src="{static}/images/chickens-on-beach.png" alt="A computer generated image of three chickens on a beach" />
    <figcaption>Created by DALL·E</figcaption>
</figure>

It's been well over three years since I've blogged, and a lot has happened in that time (I now have had two jobs in tech!) and you can hear more about at least the first part of that journey on my [podcast](https://aqoc.dev) (which is on a long term hiatus at the moment!). I recently re-read the [first post]({filename}/posts/why-am-i-learning.md) and doing so reminded me of one of the reasons I was intially drawn to a career in tech, which was artificial intelligence. On the back of this, I've started looking into machine learning and as part of this exploration I had recommended to me the fast.ai course [Practical Deep Learning](https://course.fast.ai). This is looking at creating machine learning models from the outside in (actually working with the models first, and then gradually diving deeper to understand how they work).

I've just finished the second week of the course and as part of this they challenge you to go out and create your own models based on something you're interested in. For the last year my wife and I have kept ex-battery chickens in our back garden, and something that's been invaluable is the reddit group [r/BackyardChickens](https://www.reddit.com/r/BackYardChickens/). One thing that always pops up is people asking for people to work out the breed of chicken, so I thought this is something I could turn a machine learning model to!

One of the things that people look for in machine learning models is accuracy, and I had a go at creating one and mananged to get roughly 98% accuracy! Unfortunately this was only for four breeds of chicken, and there are hundreds if not thousands of chicken breeds the world over. The other thing that people often think when hearing about machine learning is that you need _loads_ of data. I've learnt that this isn't necessarily true, as long as you start your model off by building on a pretrained model. In my case that model was called `resnet` and this is a model that has been trained on real world images (but not necessarily chickens). I think took this model and 'fine tuned' it to look specifically for chicken breeds.

You can see how the model works (and how simple the code is) [here on Kaggle](https://www.kaggle.com/code/edkenthazledine/chicken-breed-predictor-98-accuracy). Kaggle is a great site where machine learning competitions are held and you can also create your Juptyer notebooks (amongst lots of other things). If you'd like to give the chicken breed predictor a test [you can find it here](https://huggingface.co/spaces/edthecoder/chicken_breeds).

I'm planning on doing some more technical posts deep diving into areas of machine and deep learning I find interesting/hard soon, so keep an eye out!