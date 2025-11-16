from rest_framework import serializers
from .models import Character, Attribute, InventoryItem, Race, Class, Skill, Spell, Type, Item


class RaceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Race
        fields = "__all__"


class ClassModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = "__all__"


class SkillModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"


class SpellModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spell
        fields = "__all__"


class TypeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = "__all__"


class ItemModelSerializer(serializers.ModelSerializer):
    type = TypeModelSerializer(read_only=True)
    class Meta:
        model = Item
        fields = "__all__"


class ItemWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"

    def name_validat(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Длина не может быть меньше 2")
        elif len(value) > 2:
            raise serializers.ValidationError("Длина не может быть больше 2")

    def description_validat(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Длина не может быть меньше 2")
        elif len(value) > 3000:
            raise serializers.ValidationError("Длина не может быть больше 3000")


class CharacterModelSerializer(serializers.ModelSerializer):
    race = RaceModelSerializer(read_only=True)
    character_class = ClassModelSerializer(read_only=True)
    skill = SkillModelSerializer(many=True, read_only=True)
    spell = SpellModelSerializer(many=True, read_only=True)
    class Meta:
        model = Character
        fields = "__all__"
        read_only_fields = ["created_at"]


class CharacterWriteSerializer(serializers.ModelSerializer):
    race = serializers.PrimaryKeyRelatedField(queryset=Race.objects.all())
    character_class = serializers.PrimaryKeyRelatedField(queryset=Class.objects.all())
    skill = serializers.PrimaryKeyRelatedField(queryset=Skill.objects.all(), many=True)
    spell = serializers.PrimaryKeyRelatedField(queryset=Spell.objects.all(), many=True)
    class Meta:
        model = Character
        fields = "__all__"

    def level_validat(self, value):
        if value < 0:
            raise serializers.ValidationError("Значение не может быть меньше 0")
        elif value > 1000:
            raise serializers.ValidationError("Значение не может быть больше 1000")

    def name_validat(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Длина не может быть меньше 2")
        elif len(value) > 255:
            raise serializers.ValidationError("Длина не может быть больше 255")

    def backstory_validat(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Длина не может быть меньше 2")
        elif len(value) > 5000:
            raise serializers.ValidationError("Длина не может быть больше 5000")


class AttributeModelSerializer(serializers.ModelSerializer):
    character = CharacterModelSerializer(read_only=True)
    class Meta:
        model = Attribute
        fields = "__all__"


class AttributeWriteSerializer(serializers.ModelSerializer):
    character = serializers.PrimaryKeyRelatedField(queryset=Character.objects.all())
    class Meta:
        model = Attribute
        fields = "__all__"

    def strength_validat(self, value):
        if value < 0:
            raise serializers.ValidationError("Не может быть меньше 0")
        elif value > 1000:
            raise serializers.ValidationError("Не может быть больше 1000")

    def dexterity_validat(self, value):
        if value < 0:
            raise serializers.ValidationError("Не может быть меньше 0")
        elif value > 1000:
            raise serializers.ValidationError("Не может быть больше 1000")

    def constitution_validat(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Длина не может быть меньше 2")
        elif len(value) > 2:
            raise serializers.ValidationError("Длина не может быть больше 2")

    def intelligence_validat(self, value):
        if value < 0:
            raise serializers.ValidationError("Не может быть меньше 0")
        elif value > 1000:
            raise serializers.ValidationError("Не может быть больше 1000")

    def wisdom_validat(self, value):
        if value < 0:
            raise serializers.ValidationError("Не может быть меньше 0")
        elif value > 1000:
            raise serializers.ValidationError("Не может быть больше 1000")

    def charisma_validat(self, value):
        if value < 0:
            raise serializers.ValidationError("Не может быть меньше 0")
        elif value > 1000:
            raise serializers.ValidationError("Не может быть больше 1000")


class InventoryItemModelSerializer(serializers.ModelSerializer):
    character = CharacterModelSerializer(read_only=True)
    item = ItemModelSerializer(read_only=True)
    class Meta:
        model = InventoryItem
        fields = "__all__"


class InventoryItemWriteSerializer(serializers.ModelSerializer):
    character = serializers.PrimaryKeyRelatedField(queryset=Character.objects.all())
    item = serializers.PrimaryKeyRelatedField(queryset=Item.objects.all())
    class Meta:
        model = InventoryItem
        fields = "__all__"

    def quantity_validat(self, value):
        if value < 0:
            raise serializers.ValidationError("Не может быть меньше 0")
        elif value > 1000:
            raise serializers.ValidationError("Не может быть больше 1000")