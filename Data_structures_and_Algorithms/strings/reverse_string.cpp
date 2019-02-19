// logic: property of xor: associative - a^(b^c) = (a^b)^c; x=a and y=b
// first x = a^b
// y = b^x = b^(a^b) = a^(b^b) = a^0 = a
// x = a^(b^a) = (a^a)^b    = 0^b = b

string reverse_str(string str, int start, int end){
    while (start< end){

        str[start]^=str[end];
        str[end]^=str[start];
        str[start]^=str[end];

        ++start;
        --end;

    }
    return str;
}