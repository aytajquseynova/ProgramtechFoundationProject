//The getDay() method returns the weekday as a number between 0 and 6.


let day;
switch(new Date().getDay()){
    case 0:
        day="Bazar ertesi";
        break;
        case 1:
            day="Cersenbe axsami";
            break;
            case 2:
                day="Cersenbe";
                break;
                case 3:
                    day="Cume axsami";
                    break;
                    case 4:
                        day="Cume";
                        case 5:
                            day="Senbe";
                            break;
                            case 6:
                                day="Bazar";
}
document.write("Bugun"+" "+day+ " "+"gunudur.")
