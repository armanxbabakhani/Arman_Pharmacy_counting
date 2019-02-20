MAIN_DIR=`pwd`
cd $MAIN_DIR/input

find . -name "*.txt" -exec python3 $MAIN_DIR/src/Arman_pharmacy.py {} \;

if [ -e top_cost_drug.txt ];
then
        mv top_cost_drug.txt $MAIN_DIR/output/
        echo "The output file is successfully generated. Your data is sorted!"
else
        echo "The output file is not found. Something might be wrong in the code!"
fi
