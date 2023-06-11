import json
from rest_framework import authentication, permissions
from rest_framework.viewsets import ModelViewSet

class LoginRequiredModelViewSet(ModelViewSet):
    authentication_classes = (authentication.SessionAuthentication,authentication.TokenAuthentication)
    permission_classes = (permissions.IsAuthenticated,)

    def filter_by_or_operator(self,queryset,query_params):
        _queryset=queryset.none()
        for param_name,param_value in query_params.items():
            try:
                _queryset |= queryset.filter(**{param_name:param_value})
            except:
                pass
        return _queryset

    def filter_by_and_operator(self,queryset,query_params):
        for param_name,param_value in query_params.items():
            try:
                queryset = queryset.filter(**{param_name:param_value})
            except:
                pass
        return queryset

    def build_query_filter(self):
        filters={}
        for param_name,param_value in self.request.query_params.items():
            try:
                param_value = json.loads(param_value)
            except Exception as e:
                pass
                # print(self.request.query_params)
                # print(f'{param_value} is not a valid Json value to load->login_required_model_viewset->build_query_filter')
            if param_value != '':
                filters[param_name]=param_value
        return filters
            
    def filter_queryset(self, queryset):
        queryset = super(LoginRequiredModelViewSet,self).filter_queryset(queryset)
        operator = self.request.query_params.get('operator','and')
        filters=self.build_query_filter()
        if operator=='and':
            return self.filter_by_and_operator(queryset,filters)
        return self.filter_by_or_operator(queryset,filters)
        


    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response_serializer_class= self.get_response_serializer_class()
        response.data=response_serializer_class(response.data.serializer.instance).data
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        response_serializer_class= self.get_response_serializer_class()
        response.data=response_serializer_class(response.data.serializer.instance).data
        return response

    def get_response_serializer_class(self):
        return self.get_serializer_class()