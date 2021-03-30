from rest_framework.response import Response
from rest_framework.views import APIView
import datetime


class TimeNowView(APIView):
    """Вывод текущей даты и времени"""

    def get(self, request):
        time_now = datetime.datetime.now().strftime('%d/%m/%Y %H:%M')
        return Response(time_now)
