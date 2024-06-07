# -*- coding: utf-8 -*-

import re
class PasswordChecker:
    @staticmethod
    def check_strength(password):
        """Check password"""
        if not re.search(r"[A-Z]", password) or not re.search(r"[a-z]", password) or not re.search(r"\d", password):
            return "Пароль должен содержать хотя бы одну заглавную букву, одну маленькую букву и одну цифру."

        if len(password) < 8:
            return "Пароль должен содержать минимум 8 символов."

        if not re.match(r"^[A-Za-z0-9_]+$", password):
            return "Пароль должен состоять из английских букв, цифр и знака подчеркивания."
        return "Пароль надежный."