class Solution:
    def DFS(self, Digits, Sequences):
        # DFS로 맨 마지막 leaf에 도달하면 정답에 추가
        if len(Sequences) == self.lenChar:
            self.Answer.append("".join(Sequences))
        # Digits가 남아있다는 뜻 = 아직 DFS가 leaf에 도달하지 않았다는 뜻
        # Digits[:]로 넘겨주는 이유: 깊은 복사
        if Digits:
            NewSeq = Digits.pop(0)
            NewChars = self.Dict[NewSeq]
            for Char in NewChars:
                self.DFS(Digits[:], Sequences + [Char])
        
    def letterCombinations(self, digits) :
        if not digits:
            return []
        
        Digits = list(digits)        
        self.Answer = []
        self.lenChar = len(Digits)

        # Dictionary 생성
        self.Dict = dict({
            '2':list("abc"),
            '3':list("def"),
            '4':list("ghi"),
            '5':list("jkl"),
            '6':list("mno"),
            '7':list("pqrs"),
            '8':list("tuv"),
            '9':list("wxyz")
        })
        
        self.DFS(Digits[:], [])
        return self.Answer