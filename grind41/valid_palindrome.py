""" Step2

�ǂ����Ĉȉ��̃R�[�h�������Ă��܂����̂��l����

�E�ЂƂ̃X�e�b�v�ł��ׂĂ��I��点�悤�Ƃ������Ă����D
�Eright�̏��������ԈႦ�Ă���
�E��L�܂߂ďꍇ�����������ł��Ă��Ȃ��i�ǂ̒i�K�ŉ���ۏ؂������̂����V���v���ɐ�������悤�ɂ���j

"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)
        while left < right:
            while left < len(s) and not s[left].isalnum():
                left += 1
            while right > 0 and not s[right].isalnum():
                right -= 1
            if left >= right or s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True