## Picture-to-Cross-stitcher
Python Project to convert image files (e.g. JPEG, PNG etc..) into cross-stitch patterns. To do so, images are processed into bins of pixels and interpolation of RGB values yields new RGB values for the pixelated cross-stitch patterns by a mixture of mean and mode operations. The interpolated RGB values are then colour matched to the most commonly occurring RGB colours in the original image. To limit the number of thread colours required to make a cross-stitch pattern, the user can input a maximum no. of colours when building the pattern.

## Image Loader
Images are loaded to numpy arrays of RGB values via the Image module of the Pillow package PIL - implemented in the class `imgObj`, with methods open, load pixels and extract image dimensions. Execution of methods is dependent on a valid filepath to the image. 
## Picture to Pixels
Loaded Images are represented as numpy arrays of RGB values. As the width and height of images in pixels can be very high, the desired pattern is likely to have far fewer stitches than pixels. Also, to maintain image scaling, pixels are to be interpreted in square groupings. 

As a result, valid pattern sizes should have dimensions which are common factors of the image pixel counts in widht and height. To compute common factors, functions to compute numerical features are included in `numerical_features.py`. The user is able to select the desired pattern dimensions from a list using the CLI which utilise the `user_inputs.py` script.

The `pic2pix` class object is instantiated with the loaded image and once the desired pattern size has beem selected, methods to calculate the mean, mode and standard deviation of RGB pixel groups are used in the pixel_interpolator method to convert original pixels into a single RGB colour per group. By default, the mean of colours is used unless the standard deviations exceed a given value. Iteration over each pixel group is performed by the pixel_iterator method to return an array of interpolated RGB values matching the desired pattern scheme.  

Once created, colour matching can be performed to reduce the number of colours in the final pattern. 
## Colour Matching
To limit the number of colours in the cross-stitch design, the interpolated colours are matched to the closest colours available from a list of most common RGB values in the original image.

Colour matching was first implemented by minimising distances in the 3-D space of RGB values, nominally the root sum of square differences (RSSD) between two colours. In this approach however, it becomes possible to generate several colours which are deemed equidistant from a target colour. 

For example:

Target RGB $= (110,150,13)$
Optn A RGB $= (111,150,25)$
Optn B RGB $= (100,156,10)$
match measure A = $\sqrt{(110-111)^2 + (150-150)^2 + (13-25)^2} = \sqrt{145}$
match measure B = $\sqrt{(110-100)^2 + (150-156)^2 + (13-10)^2} = \sqrt{145}$

Further investigation yields the inadequacies of RGB 3D spatial distance measures alone to replicate colour similarities as observed by humans. For those interested, conflicting methods around CIE L*a*b* and CIE L*u*v* to compute percieved colour from RGB values exist with deficiencies in each approach - an article by Thiadmer Riemersma on the efficacies of the approaches can be found here: https://www.compuphase.com/cmetric.htm 

In the above article, the author proposes a similar euclidean norm with additional weighting based on the magnitude of red R values in the target and proposed colours. This approach is underpinned by the notion that human differences in colour perception of red in RGB follows a logarithmic scale and as such a euclidean norm alone will not capture these differences. This method has been implemented in `colour_match_extract.py - colour_similarity_riemersma` - it doesn't purport to wholly accurate but does represent a simplistic improvement on the spatial norm approach alone.

While this produces satisfactory results, the response can be hindered by utilisation of the most frequent colours in the original image only. To improve this, optimisation functions to maximise colour divergence in the colours selected are to be implemented to help avoid explicitly defining all desired 23 colours as being shades of light-blue (or grey when in Manchester) because of a patch of sky in the original image. This is the subject of ongoing development.
## Thread Databases
Subject of future work to provide a reference MySQL database of RGB:thread colours
