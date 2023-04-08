from rest_framework import serializers
from base.models import Item, Student

class ItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class StudentSerializers(serializers.ModelSerializer):
    new_tuition = serializers.SerializerMethodField(method_name='calc_age')
    rename = serializers.CharField(max_length=25, source='name')
    class Meta:
        model = Student
        fields = ['id', 'rename', 'age', 'tuition', 'new_tuition', 'featured_item']

    def calc_age(self, student: Student):
        return student.tuition * 2.1

class StudentAddSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
