function solution(brown, yellow) {
    let h,w;
   for (h=0; h <= Math.sqrt(yellow); h++){
       if (yellow % h) continue;
       w = yellow/h;
       if ((w*2+h*2+4)===brown) break;
   }
    return [w+2, h+2];
}