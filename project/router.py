#khusus personal_journal(journal) versi app
from journal.viewset import JournalViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('journal',JournalViewset)

