from django.db import models

class Players(models.Model):
    name = models.CharField(max_length=264, unique=True)


    def player_score_board(self):
        print('HERE......>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>',self.player_scores)
        return self.player_scores

    def __str__(self) -> str:
        return str(self.name)


class LeadBoard(models.Model):
    name = models.ForeignKey(Players,  related_name='player_scores', on_delete=models.CASCADE)
    score = models.FloatField(default=0)
    

    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.name.name+'('+str(self.score)+')'