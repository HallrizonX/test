import os

from django.http import FileResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication
from rest_framework.parsers import FileUploadParser

from .serializers import RunnerPythonSerializer
from .CMD import CMDFactory


class RunnerPython(APIView):
    authentication_classes = [authentication.TokenAuthentication]

    def get(self, request):
        serializer = RunnerPythonSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors)

        cmd, code = serializer.data['cmd'], serializer.data['code']
        cmd = CMDFactory.get(cmd, code)
        try:
            cmd.execute()
        except BaseException:
            cmd.result, cmd._code = 'None', 'None'

        return Response(data={"result": cmd.result, "code": cmd.get_code})


class StaticFiles(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    DIR = 'static/'
    parser_classes = (FileUploadParser,)

    def get(self, request):
        filename = request.data['filename']
        file = None
        with open(f'{self.DIR}{filename}', 'r') as f:
            file = f.read()
        return FileResponse(file)

    def post(self, request):
        file_obj = request.FILES['file']

        return Response(status=204)
