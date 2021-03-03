DIR="$( cd "$( dirname "$0" )" && pwd )"
alias python=python3

python "$DIR/phase1/facebook.py" &
python "$DIR/phase1/instagram.py" &
python "$DIR/phase2/facebook.py" &
python "$DIR/phase2/instagram_posttype.py" &
python "$DIR/phase2/reviews.py" &
python "$DIR/phase2/competitors.py" &
python "$DIR/phase2/postdate_difference.py" & 
python "$DIR/phase2/influencer_engagement.py"  

