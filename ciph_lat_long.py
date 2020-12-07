import geo
import string

class encoded_integers():
    p1 = geo.geo_location()
    lo = p1.lng
    la = p1.lat
    li = list(map(int, str(lo)))
    lii = list(map(int, str(la)))
    fi = []
    fii = []

   ###  '''for encoding the city and state of the location traced'''
    #traced_city = p1.ci
    #traced_state = p1.sta
    #lc = list(map(str, str(traced_city.lower())))
    #ls = list(map(str, str(traced_state.lower())))
    #lc_upper = list(map(str, str(traced_city.upper())))
    #ls_upper = list(map(str, str(traced_state.upper())))


    '''now we will merge the lists of city and state such that all the alphabets of city and state 
    are present in a single list such that it would be easy to eliminate the alphabets from the parent list'''
    #lower_location_list = list(set(lc+ls))
    #upper_location_list = list(set(lc_upper+ls_upper))


    #l_lower_alpha = list(map(str,str(string.ascii_lowercase)))
    #l_upper_alpha = list(map(str,str(string.ascii_uppercase)))
    '''now we shall remove the location list from the respective parent list'''
    #for i1 in lower_location_list:
        #try:
            #l_lower_alpha.remove(i1)
        #except ValueError:
           # pass


    '''for upper case list filtering'''
    #for i2 in upper_location_list:
        #try:
     #       l_upper_alpha.remove(i2)
      #  except ValueError:
       #     pass



    '''now we shall convert all the list of filtered location details to a string of aplhabets'''

    #def convert(s):

        # initialization of string to ""
     #   str1 = ""

        # using join function join the list s by
        # separating words by str1
      #  return (str1.join(s))
    '''this is the alphabetical encoded data'''
    #encoded_lower_location = convert(l_lower_alpha)
    #encoded_upper_location = convert(l_upper_alpha)


    '''for encoding logitude data'''
    for n in range(0, len(li)):
        p = li[n] % 2
        i = n + 1
        if (p == 1):
            # multiply with immediate odd number(right side)
            a = []
            for j in range(i, len(li)):
                if (li[j] % 2 != 0):
                    k = li[j]
                    a.append(k)
            if (len(a) != 0):
                b = li[n] * a[0]
            else:
                b = li[n]

            # multiply with even powers
            a1 = []
            for j in range(i - 2, 0, -1):
                if (li[j] % 2 == 0):
                    k = li[j]
                    a1.append(k)
            if (len(a1) != 0):
                c = b * (a1[0] ** a1[0])
            else:
                c = b

            fi.append(c)
        # if number is even
        else:
            # multiply with immediate even number (left side)
            d = []
            for j in range(i - 2, 0, -1):
                if (li[j] % 2 == 0):
                    k = li[j]
                    d.append(k)
            if (len(d) != 0):
                b = li[n] * d[0]
            else:
                b = li[n]
            # multiply with odd powers
            d1 = []
            for j in range(i, len(li)):
                if (li[j] % 2 != 0):
                    k = li[j]
                    d1.append(k)
            if (len(d1) != 0):
                e = b * (d1[0] ** d1[0])
            else:
                e = b

            fi.append(e)

    '''for encoding latitude data'''
    for nn in range(0, len(lii)):
        pp = lii[nn] % 2
        ii = nn + 1
        if (pp == 1):
            # multiply with immediate odd number(right side)
            aa = []
            for jj in range(ii, len(lii)):
                if (lii[jj] % 2 != 0):
                    kk = lii[jj]
                    aa.append(kk)
            if (len(aa) != 0):
                bb = lii[nn] * aa[0]
            else:
                bb = lii[nn]

            # multiply with even powers
            aa1 = []
            for jj in range(ii - 2, 0, -1):
                if (lii[jj] % 2 == 0):
                    kk = lii[jj]
                    aa1.append(kk)
            if (len(aa1) != 0):
                cc = bb * (aa1[0] ** aa1[0])
            else:
                cc = bb

            fii.append(cc)
        # if number is even
        else:
            # multiply with immediate even number (left side)
            dd = []
            for jj in range(ii - 2, 0, -1):
                if (lii[jj] % 2 == 0):
                    kk = lii[jj]
                    dd.append(kk)
            if (len(dd) != 0):
                bb = lii[nn] * dd[0]
            else:
                bb = lii[nn]
            # multiply with odd powers
            dd1 = []
            for jj in range(ii, len(lii)):
                if (lii[jj] % 2 != 0):
                    kk = lii[jj]
                    dd1.append(kk)
            if (len(dd1) != 0):
                ee = bb * (dd1[0] ** dd1[0])
            else:
                ee = bb

            fii.append(ee)

    '''we will combine the list that we had produced into a string of integers'''

    def concatenate_list_data(list):
        result = ''
        for element in list:
            result += str(element)
        return result

    '''converting the list of encoded longitude and latitude data taken'''
    lng_data = int(concatenate_list_data(fi))
    lat_data = int(concatenate_list_data(fii))
    encoded_coord_data = abs((lng_data+lat_data)*(lng_data-lat_data))




