# jpg2pdf
## this project is for me to convert a comic picture to a pdf file for kindle.

#Features
* cross platform
* recursion supported
* different model supported

#Usage

    import jpg2pdf

##Parameters

path : string
       path of the pictures

recursion : boolean
       None or False for no recursion
       True for recursion to children folder
       wether to recursion or not
    
pictureType : list
              type of pictures,for example :jpg,png...
sizeMode : int 
           None or 0 for pdf's pagesize is the biggest of all the pictures
           1 for pdf's pagesize is the min of all the pictures
           2 for pdf's pagesize is the given value of width and height
           to choose how to determine the size of pdf
    
width : int
        width of the pdf page

height : int
         height of the pdf page

fit : boolean
      None or False for fit the picture size to pagesize
           True for keep the size of the pictures
           wether to keep the picture size or not

save : string 
       path to save the pdf 

#TODO

* a better gui