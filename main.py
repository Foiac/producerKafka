from infrastructure.service.storerevies import storereviews
from infrastructure.messaging.producerkafka import producerkafka
from domain.entities.review import reviewEntity
from interactor.dtos.reviewDTO import reviewDTO
from json import loads
import json 
from datetime import datetime 

class main():

    if __name__ == "__main__":

        reviews = storereviews()
        #my_reviews = reviews.getReviews('com.santander.app')
        my_reviews = reviews.getAllReviews('com.santander.app')
        kafka_producer = producerkafka('localhost:9093', 'Post.Review') 

        for i in range(len(my_reviews)):
            reviewE = reviewEntity(**my_reviews[i])

            reviewD = reviewDTO(reviewE.reviewId, 
                                reviewE.userName,
                                reviewE.userImage,
                                reviewE.content,
                                reviewE.score,
                                reviewE.thumbsUpCount,
                                reviewE.reviewCreatedVersion,
                                reviewE.at.strftime("%Y-%m-%dT%H:%M:%S"),
                                reviewE.replyContent,
                                reviewE.repliedAt,
                                reviewE.appVersion
                                )

            reviewString = json.dumps(reviewD._asdict(), default=str)
            reviewJson = json.loads(reviewString)
            kafka_producer.sendJson(reviewJson)

main()