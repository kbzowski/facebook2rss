from .main.login import LoginPage as MainLoginPage
from .mbasic.group import GroupPage as MBasicGroupPage
from .mbasic.login import LoginPage as MBasicLoginPage
from .mbasic.login_checkpoint import LoginCheckpointPage as MBasicLoginCheckpointPage
from .mbasic.notification import NotificationPage as MBasicNotificationPage
from .mbasic.page import FBPage as MBasicPage
from .mbasic.profile import ProfilePage as MBasicProfilePage
from .mobile.login import LoginPage as MobileLoginPage

pages = {
    "main": {
        "login": MainLoginPage
    },
    "mobile": {
        "login": MobileLoginPage
    },
    "mbasic": {
        "login": MBasicLoginPage,
        "login_checkpoint": MBasicLoginCheckpointPage,
        "profile": MBasicProfilePage,
        "page": MBasicPage,
        "group": MBasicGroupPage,
        "notification": MBasicNotificationPage
    }
}
