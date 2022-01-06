from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm.session import Session
from .. import schemas, database, models, oauth2

router = APIRouter(
    prefix="/vote",
    tags=['vote']
)
@router.post("/", status_code=status.HTTP_201_CREATED)
def vote(vote: schemas.Vote, db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):

    post = db.query(models.Post).filter(models.Post.id == vote.post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {vote.post_id} does not exist")

    vote_query = db.query(models.Vote).filter(models.Vote.post_id == vote.post_id, models.Vote.user_id == current_user.id)
        # first check to see if there is already vote for this post.id
        # second check if specific user already voted for this post (after comma)

    found_vote = vote_query.first()
    # performed query
    if (vote.dir == 1):
        if found_vote:
                raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"user {current_user.id} has already voted on post {vote.post_id}")
                # if we found a vote
        new_vote = models.Vote(post_id = vote.post_id, user_id=current_user.id)
        # if we found vote
        # set 2 properties
        db.add(new_vote)
        # performed changes
        db.commit()
        # saved ones
        return {"message": "successfully added vote"}
        # we don't need to send created query
    else:
        if not found_vote:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vote does not exist")
        # you can't delete post that not exist
        vote_query.delete(synchronize_session=False)
        # deleting vote if it exist
        db.commit()
        # saving changes
        return {"message" : "successfully deleted vote"}