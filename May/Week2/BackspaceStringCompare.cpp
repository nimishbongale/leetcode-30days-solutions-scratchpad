class Solution {
public:
    stack <char> s;
    string ps(){ 
        string r="";
        while (!s.empty()) 
        { 
            r+=s.top(); 
            s.pop(); 
        } 
        return r;
    }
    
    string l(string K){
        for(auto x:K)
            if(s.empty()&&x=='#')
                continue;
            else if(x=='#'&&!s.empty())
                s.pop();
            else
                s.push(x);
        return ps();
    }
    bool backspaceCompare(string S, string T) {
        cout<<l(S)<<"    "<<l(T);
        if(l(S)==l(T))
            return true;
        return false;
    }
};
