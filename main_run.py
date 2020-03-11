from download_data import downloadDataF
from user_posts import userPostsF
from titles import titlesF
from duplicate_titles import duplicatesF
from close_neighbors import whoIsCloserF

def runScript():
    downloadDataF()
    titlesF()
    duplicatesF()
    whoIsCloserF()

runScript()
