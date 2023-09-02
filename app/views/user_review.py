from django.shortcuts import render, redirect
from django.db.models import Avg
from ..models import Review, Matching
from ..forms.review import ReviewForm

def rate_seller(request, matching_id):
    matching = Matching.objects.get(id=matching_id)
    seller = matching.seller
    buyer = matching.buyer

    if request.method == 'POST':
        score = int(request.POST['rater'])
        text = request.POST['text']

        review = Review.objects.create(rater=matching, evaluator=matching, score=score, text=text)
        review.save()
        # Calculate average rating for the seller
        average_rating = Review.objects.filter(evaluator=matching).aggregate(Avg('score'))['score__avg']
        seller.average_rating = average_rating
        seller.save()

        return redirect('match')

    return render(request, 'review/review.html', {'matching': matching})
