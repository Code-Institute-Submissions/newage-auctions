from django.utils import timezone

from celery import shared_task 
from celery.utils.log import get_task_logger

from auction.models import Auction, Bid


logger = get_task_logger(__name__)


@shared_task(name='auction.tasks.task_set_auction_to_expire') 
def task_set_auction_to_expire():
    """
    Set auction.expired to True if the auction is over.
    Filter the bids for the auction, find the last bid made and set the winner
    who bidded last.
    If no bid found save the auction and log.
    """
    auctions = Auction.objects.all()

    for auction in auctions:
        if auction.expired != True: 
            if auction.time_ending < timezone.now():
                auction.expired = True
                bid = Bid.objects.filter(auction=auction.pk).order_by('-bid_time')
                if bid:                                 
                    latest_bid = bid[0]
                    auction.winner = latest_bid.user
                    auction.winning_bid = latest_bid.bid_amount
                    auction.save()
                    logger.info("Expired and winner set.")
                else:
                    auction.save()
                    logger.info("Bid not found")
            else:
                logger.info("Auction not expired, aborted function")
            

    