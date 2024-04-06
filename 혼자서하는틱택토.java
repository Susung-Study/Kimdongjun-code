class Solution {
    public int solution(String[] board) {
        int xnum = countox(board,'X');
        int onum = countox(board,'O');
        
        if (xnum > onum ||onum > xnum + 1) {
            return 0;
        }

        if (hasWon(board, 'O')) {
            if (onum <= xnum) {
                return 0;
            }
        }
        
        if (hasWon(board, 'X')) {
            if (onum >= xnum + 1) {
                return 0;
            }
        }
        
        return 1;
    }
    
    private int countox(String[] board, char ch){
        int result = 0;
        for(int i = 0; i<3; i++){
            for(int j = 0; j<3; j++){
                if(board[i].charAt(j)==ch){
                    result++;
                }
            }
        }
        return result;
    }
    
    private boolean hasWon(String[] board, char ch){
        for(int i =0; i<3; i++){
            if(board[i].charAt(0)==ch
              && board[i].charAt(1)==ch
              && board[i].charAt(2)==ch){
                return true;
            }
        }
        
        for(int i=0; i<3; i++){
            if(board[0].charAt(i)==ch
              && board[1].charAt(i)==ch
                && board[2].charAt(i)==ch){
                return true;
            }
        }
        
        if(board[0].charAt(0) == ch
          && board[1].charAt(1) == ch
          && board[2].charAt(2) == ch){
            return true;
        }
        
        if(board[0].charAt(2) == ch
          && board[1].charAt(1) == ch
          && board[2].charAt(0) == ch){
            return true;
        }
        return false;
    }
}